// Copyright (c) Alexander Rind & the SoniVis team.
// Distributed under the terms of the MIT License (see LICENSE).
// h/t <https://d3-graph-gallery.com/graph/parallel_basic.html>

import { DOMWidgetView } from '@jupyter-widgets/base';
import * as d3a from 'd3-array';
import { axisLeft } from 'd3-axis';
import * as d3s from 'd3-selection';
import * as d3sc from 'd3-scale';
import { schemeTableau10 } from 'd3-scale-chromatic';
import { line as d3line } from 'd3-shape';
// import * as d3sh from 'd3-shape';

const MARGIN = { top: 20, right: 10, bottom: 5, left: 30 };
const LEGEND_WIDTH = 50;

export class ParChords {
  private view: DOMWidgetView;

  constructor(view: DOMWidgetView) {
    this.view = view;

    const g = d3s
      .select(view.el)
      .append('svg')
      .attr('width', 100)
      .attr('height', 100)
      .append('g')
      .classed('substrate', true)
      .attr('transform', 'translate(' + MARGIN.left + ',' + MARGIN.top + ')');

    // add the color legend
    g.append('g')
      .attr('id', 'legend')
      .append('text')
      .classed('label', true)
      .style('text-anchor', 'end');

    // this.lensCursor = new LensCursor(view, g);

    this.updateSubstrateSize();
    this.view.model.on(
      'change:width change:height',
      () => this.updateSubstrateSize(),
      this.view
    );
    this.view.model.on(
      'change:_marks_val change:_marks_color',
      this.updateData,
      this
    );
  }

  private updateSubstrateSize() {
    const width = this.view.model.get('width') as number;
    const height = this.view.model.get('height') as number;

    d3s
      .select(this.view.el)
      .select('svg')
      .attr('width', width)
      .attr('height', height);

    this.updateData();
  }

  private updateData() {
    const fields = this.view.model.get('axis_fields') as string[];
    const values = this.view.model.get('_marks_val') as number[][];
    const cValues = this.view.model.get('_marks_color') as string[];

    const colorValues = d3a
      .rollups(
        cValues,
        (v) => v.length,
        (d) => d
      )
      .sort((a, b) => (a[1] < b[1] ? 1 : -1))
      .map((v) => v[0]);

    const colorScale = d3sc.scaleOrdinal(schemeTableau10).domain(colorValues);

    const substWidth =
      (this.view.model.get('width') as number) -
      MARGIN.left -
      (colorValues.length > 0 ? LEGEND_WIDTH : MARGIN.right);
    const substHeight =
      (this.view.model.get('height') as number) - MARGIN.top - MARGIN.bottom;

    // set the scales
    const axisScale = prepareAxeScale(fields, [0, substWidth]);
    const valueScales = prepareValueScales(fields, values, [substHeight, 0]);

    const gSubstrate = d3s.select(this.view.el).select('g.substrate');

    // helper function that turns an item array to coordinate pairs
    const pathGenerator = d3line()
      .x((_v, vi) => axisScale(fields[vi]) as number)
      .y((v, vi) => valueScales[vi](v as unknown as number));

    // encode each item into a path
    gSubstrate
      .selectAll('path')
      .data(values)
      .join('path')
      .attr('d', pathGenerator as any)
      .style('fill', 'none')
      .style('stroke', (_d, i) => colorScale(cValues[i]))
      .style('opacity', 0.5);

    // draw the parallel axes
    gSubstrate
      .selectAll('g.pcaxis')
      // for each field of the dataset -> add a 'g' element and have its name as key
      .data(fields, (d) => d as string)
      .join((enter) =>
        enter
          .append('g')
          .classed('pcaxis', true)
          // important to call 'text', so that g is returned by enter() function
          .call((enter) =>
            enter
              .append('text')
              .style('text-anchor', 'middle')
              .attr('y', -9)
              .text((d) => d)
              .style('fill', 'black')
              .on('click', (_evt, datum) => {
                // console.log('axis click: ' + datum);
                this.view.send({
                  event: 'axis_click',
                  field: datum,
                });
              })
          )
      )
      // on enter and update -> translate the g element to its horizontal position
      .attr('transform', (d) => 'translate(' + axisScale(d) + ')')
      .each(function (d, i) {
        d3s.select(this).call(axisLeft(valueScales[i]) as any);
      });

    // update the legend
    const gLegend = gSubstrate.select('g#legend');
    gLegend.attr(
      'transform',
      'translate(' + (substWidth + LEGEND_WIDTH) + ', -2)'
    );
    gLegend.select('text.label').text(this.view.model.get('color_field'));

    gLegend
      .selectAll('text.axis')
      .data(colorValues)
      .join('text')
      .attr('class', 'axis')
      .text((d: string) => d)
      .style('text-anchor', 'end')
      .attr('x', -9)
      .attr('y', (d, i) => i * 14 + 14);

    gLegend
      .selectAll('rect')
      .data(colorValues)
      .join('rect')
      .attr('x', -7)
      .attr('y', (d, i) => i * 14 + 10)
      .attr('width', 7)
      .attr('height', 2)
      .style('fill', (d: string) => colorScale(d));
  }
}

function prepareAxeScale(
  fields: string[],
  range: Iterable<number>
): d3sc.ScalePoint<string> {
  return d3sc.scalePoint(fields, range).padding(0.1);
}

function prepareValueScales(
  fields: string[],
  values: number[][],
  range: Iterable<number>
): d3sc.ScaleLinear<number, number, never>[] {
  return fields.map((_f, fi) => {
    const vMin = d3a.min(values, (v) => v[fi]) || 0;
    const vMax = d3a.max(values, (v) => v[fi]) || 0;
    // console.log(_f + ' ' + vMin + ' ' + vMax);
    // console.log(values.map((v) => v[fi]));
    // vMax = vMax === vMin ? vMax + 1 : vMax;
    return d3sc.scaleLinear().range(range).domain([vMin, vMax]);
  });
}
