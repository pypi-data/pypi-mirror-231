(self["webpackChunkparchords_jupyter"] = self["webpackChunkparchords_jupyter"] || []).push([["lib_widget_js"],{

/***/ "./node_modules/css-loader/dist/cjs.js!./css/widget.css":
/*!**************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./css/widget.css ***!
  \**************************************************************/
/***/ ((module, exports, __webpack_require__) => {

// Imports
var ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
exports = ___CSS_LOADER_API_IMPORT___(false);
// Module
exports.push([module.id, ".custom-widget {\n  background-color: lightseagreen;\n  padding: 0px 2px;\n}\n\n.substrate .axis , #legend {\n  font-size: 10px;\n  color: #404040;\n}\n", ""]);
// Exports
module.exports = exports;


/***/ }),

/***/ "./lib/parchords.js":
/*!**************************!*\
  !*** ./lib/parchords.js ***!
  \**************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

// Copyright (c) Alexander Rind & the SoniVis team.
// Distributed under the terms of the MIT License (see LICENSE).
// h/t <https://d3-graph-gallery.com/graph/parallel_basic.html>
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ParChords = void 0;
const d3a = __importStar(__webpack_require__(/*! d3-array */ "webpack/sharing/consume/default/d3-array/d3-array?e6df"));
const d3_axis_1 = __webpack_require__(/*! d3-axis */ "webpack/sharing/consume/default/d3-axis/d3-axis");
const d3s = __importStar(__webpack_require__(/*! d3-selection */ "webpack/sharing/consume/default/d3-selection/d3-selection"));
const d3sc = __importStar(__webpack_require__(/*! d3-scale */ "webpack/sharing/consume/default/d3-scale/d3-scale"));
const d3_scale_chromatic_1 = __webpack_require__(/*! d3-scale-chromatic */ "webpack/sharing/consume/default/d3-scale-chromatic/d3-scale-chromatic");
const d3_shape_1 = __webpack_require__(/*! d3-shape */ "webpack/sharing/consume/default/d3-shape/d3-shape");
// import * as d3sh from 'd3-shape';
const MARGIN = { top: 20, right: 10, bottom: 5, left: 30 };
const LEGEND_WIDTH = 50;
class ParChords {
    constructor(view) {
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
        this.view.model.on('change:width change:height', () => this.updateSubstrateSize(), this.view);
        this.view.model.on('change:_marks_val change:_marks_color', this.updateData, this);
    }
    updateSubstrateSize() {
        console.log('updateSubstrateSize');
        const width = this.view.model.get('width');
        const height = this.view.model.get('height');
        d3s
            .select(this.view.el)
            .select('svg')
            .attr('width', width)
            .attr('height', height);
        this.updateData();
    }
    updateData() {
        const fields = this.view.model.get('axis_fields');
        const values = this.view.model.get('_marks_val');
        const cValues = this.view.model.get('_marks_color');
        const colorValues = d3a
            .rollups(cValues, (v) => v.length, (d) => d)
            .sort((a, b) => (a[1] < b[1] ? 1 : -1))
            .map((v) => v[0]);
        const colorScale = d3sc.scaleOrdinal(d3_scale_chromatic_1.schemeTableau10).domain(colorValues);
        const substWidth = this.view.model.get('width') -
            MARGIN.left -
            (colorValues.length > 0 ? LEGEND_WIDTH : MARGIN.right);
        const substHeight = this.view.model.get('height') - MARGIN.top - MARGIN.bottom;
        // set the scales
        const axisScale = prepareAxeScale(fields, [0, substWidth]);
        const valueScales = prepareValueScales(fields, values, [substHeight, 0]);
        const gSubstrate = d3s.select(this.view.el).select('g.substrate');
        // helper function that turns an item array to coordinate pairs
        const pathGenerator = d3_shape_1.line()
            .x((_v, vi) => axisScale(fields[vi]))
            .y((v, vi) => valueScales[vi](v));
        // encode each item into a path
        gSubstrate
            .selectAll('path')
            .data(values)
            .join('path')
            .attr('d', pathGenerator)
            .style('fill', 'none')
            .style('stroke', (_d, i) => colorScale(cValues[i]))
            .style('opacity', 0.5);
        // draw the parallel axes
        gSubstrate
            .selectAll('g.pcaxis')
            // for each field of the dataset -> add a 'g' element and have its name as key
            .data(fields, (d) => d)
            .join((enter) => enter
            .append('g')
            .classed('pcaxis', true)
            // important to call 'text', so that g is returned by enter() function
            .call((enter) => enter
            .append('text')
            .style('text-anchor', 'middle')
            .attr('y', -9)
            .text((d) => d)
            .style('fill', 'black')
            .on('click', (_evt, datum) => {
            console.log('axis click: ' + datum);
            this.view.send({
                event: 'axis_click',
                field: datum,
            });
        })))
            // on enter and update -> translate the g element to its horizontal position
            .attr('transform', (d) => 'translate(' + axisScale(d) + ')')
            .each(function (d, i) {
            d3s.select(this).call(d3_axis_1.axisLeft(valueScales[i]));
        });
        // update the legend
        const gLegend = gSubstrate.select('g#legend');
        gLegend.attr('transform', 'translate(' + (substWidth + LEGEND_WIDTH) + ', -2)');
        gLegend.select('text.label').text(this.view.model.get('color_field'));
        gLegend
            .selectAll('text.axis')
            .data(colorValues)
            .join('text')
            .attr('class', 'axis')
            .text((d) => d)
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
            .style('fill', (d) => colorScale(d));
    }
}
exports.ParChords = ParChords;
function prepareAxeScale(fields, range) {
    return d3sc.scalePoint(fields, range).padding(0.1);
}
function prepareValueScales(fields, values, range) {
    return fields.map((_f, fi) => {
        const vMin = d3a.min(values, (v) => v[fi]) || 0;
        const vMax = d3a.max(values, (v) => v[fi]) || 0;
        // console.log(_f + ' ' + vMin + ' ' + vMax);
        // console.log(values.map((v) => v[fi]));
        // vMax = vMax === vMin ? vMax + 1 : vMax;
        return d3sc.scaleLinear().range(range).domain([vMin, vMax]);
    });
}


/***/ }),

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// Copyright (c) Alexander Rind & the SoniVis team.
// Distributed under the terms of the MIT License (see LICENSE).
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MODULE_NAME = exports.MODULE_VERSION = void 0;
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
exports.MODULE_VERSION = data.version;
/*
 * The current package name.
 */
exports.MODULE_NAME = data.name;


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// Copyright (c) Alexander Rind & the SoniVis team.
// Distributed under the terms of the MIT License (see LICENSE).
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ParChordsView = exports.ParChordsModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
// Import the CSS
__webpack_require__(/*! ../css/widget.css */ "./css/widget.css");
const parchords_1 = __webpack_require__(/*! ./parchords */ "./lib/parchords.js");
class ParChordsModel extends base_1.DOMWidgetModel {
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: ParChordsModel.model_name, _model_module: ParChordsModel.model_module, _model_module_version: ParChordsModel.model_module_version, _view_name: ParChordsModel.view_name, _view_module: ParChordsModel.view_module, _view_module_version: ParChordsModel.view_module_version, axis_fields: [], color_field: '', _marks_val: [], _marks_color: [], width: 700, height: 400 });
    }
}
exports.ParChordsModel = ParChordsModel;
ParChordsModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
ParChordsModel.model_name = 'ParChordsModel';
ParChordsModel.model_module = version_1.MODULE_NAME;
ParChordsModel.model_module_version = version_1.MODULE_VERSION;
ParChordsModel.view_name = 'ParChordsView'; // Set to null if no view
ParChordsModel.view_module = version_1.MODULE_NAME; // Set to null if no view
ParChordsModel.view_module_version = version_1.MODULE_VERSION;
class ParChordsView extends base_1.DOMWidgetView {
    render() {
        new parchords_1.ParChords(this);
    }
}
exports.ParChordsView = ParChordsView;


/***/ }),

/***/ "./node_modules/css-loader/dist/runtime/api.js":
/*!*****************************************************!*\
  !*** ./node_modules/css-loader/dist/runtime/api.js ***!
  \*****************************************************/
/***/ ((module) => {

"use strict";


/*
  MIT License http://www.opensource.org/licenses/mit-license.php
  Author Tobias Koppers @sokra
*/
// css base code, injected by the css-loader
// eslint-disable-next-line func-names
module.exports = function (useSourceMap) {
  var list = []; // return the list of modules as css string

  list.toString = function toString() {
    return this.map(function (item) {
      var content = cssWithMappingToString(item, useSourceMap);

      if (item[2]) {
        return "@media ".concat(item[2], " {").concat(content, "}");
      }

      return content;
    }).join('');
  }; // import a list of modules into the list
  // eslint-disable-next-line func-names


  list.i = function (modules, mediaQuery, dedupe) {
    if (typeof modules === 'string') {
      // eslint-disable-next-line no-param-reassign
      modules = [[null, modules, '']];
    }

    var alreadyImportedModules = {};

    if (dedupe) {
      for (var i = 0; i < this.length; i++) {
        // eslint-disable-next-line prefer-destructuring
        var id = this[i][0];

        if (id != null) {
          alreadyImportedModules[id] = true;
        }
      }
    }

    for (var _i = 0; _i < modules.length; _i++) {
      var item = [].concat(modules[_i]);

      if (dedupe && alreadyImportedModules[item[0]]) {
        // eslint-disable-next-line no-continue
        continue;
      }

      if (mediaQuery) {
        if (!item[2]) {
          item[2] = mediaQuery;
        } else {
          item[2] = "".concat(mediaQuery, " and ").concat(item[2]);
        }
      }

      list.push(item);
    }
  };

  return list;
};

function cssWithMappingToString(item, useSourceMap) {
  var content = item[1] || ''; // eslint-disable-next-line prefer-destructuring

  var cssMapping = item[3];

  if (!cssMapping) {
    return content;
  }

  if (useSourceMap && typeof btoa === 'function') {
    var sourceMapping = toComment(cssMapping);
    var sourceURLs = cssMapping.sources.map(function (source) {
      return "/*# sourceURL=".concat(cssMapping.sourceRoot || '').concat(source, " */");
    });
    return [content].concat(sourceURLs).concat([sourceMapping]).join('\n');
  }

  return [content].join('\n');
} // Adapted from convert-source-map (MIT)


function toComment(sourceMap) {
  // eslint-disable-next-line no-undef
  var base64 = btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap))));
  var data = "sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(base64);
  return "/*# ".concat(data, " */");
}

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js":
/*!****************************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js ***!
  \****************************************************************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var isOldIE = function isOldIE() {
  var memo;
  return function memorize() {
    if (typeof memo === 'undefined') {
      // Test for IE <= 9 as proposed by Browserhacks
      // @see http://browserhacks.com/#hack-e71d8692f65334173fee715c222cb805
      // Tests for existence of standard globals is to allow style-loader
      // to operate correctly into non-standard environments
      // @see https://github.com/webpack-contrib/style-loader/issues/177
      memo = Boolean(window && document && document.all && !window.atob);
    }

    return memo;
  };
}();

var getTarget = function getTarget() {
  var memo = {};
  return function memorize(target) {
    if (typeof memo[target] === 'undefined') {
      var styleTarget = document.querySelector(target); // Special case to return head of iframe instead of iframe itself

      if (window.HTMLIFrameElement && styleTarget instanceof window.HTMLIFrameElement) {
        try {
          // This will throw an exception if access to iframe is blocked
          // due to cross-origin restrictions
          styleTarget = styleTarget.contentDocument.head;
        } catch (e) {
          // istanbul ignore next
          styleTarget = null;
        }
      }

      memo[target] = styleTarget;
    }

    return memo[target];
  };
}();

var stylesInDom = [];

function getIndexByIdentifier(identifier) {
  var result = -1;

  for (var i = 0; i < stylesInDom.length; i++) {
    if (stylesInDom[i].identifier === identifier) {
      result = i;
      break;
    }
  }

  return result;
}

function modulesToDom(list, options) {
  var idCountMap = {};
  var identifiers = [];

  for (var i = 0; i < list.length; i++) {
    var item = list[i];
    var id = options.base ? item[0] + options.base : item[0];
    var count = idCountMap[id] || 0;
    var identifier = "".concat(id, " ").concat(count);
    idCountMap[id] = count + 1;
    var index = getIndexByIdentifier(identifier);
    var obj = {
      css: item[1],
      media: item[2],
      sourceMap: item[3]
    };

    if (index !== -1) {
      stylesInDom[index].references++;
      stylesInDom[index].updater(obj);
    } else {
      stylesInDom.push({
        identifier: identifier,
        updater: addStyle(obj, options),
        references: 1
      });
    }

    identifiers.push(identifier);
  }

  return identifiers;
}

function insertStyleElement(options) {
  var style = document.createElement('style');
  var attributes = options.attributes || {};

  if (typeof attributes.nonce === 'undefined') {
    var nonce =  true ? __webpack_require__.nc : 0;

    if (nonce) {
      attributes.nonce = nonce;
    }
  }

  Object.keys(attributes).forEach(function (key) {
    style.setAttribute(key, attributes[key]);
  });

  if (typeof options.insert === 'function') {
    options.insert(style);
  } else {
    var target = getTarget(options.insert || 'head');

    if (!target) {
      throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
    }

    target.appendChild(style);
  }

  return style;
}

function removeStyleElement(style) {
  // istanbul ignore if
  if (style.parentNode === null) {
    return false;
  }

  style.parentNode.removeChild(style);
}
/* istanbul ignore next  */


var replaceText = function replaceText() {
  var textStore = [];
  return function replace(index, replacement) {
    textStore[index] = replacement;
    return textStore.filter(Boolean).join('\n');
  };
}();

function applyToSingletonTag(style, index, remove, obj) {
  var css = remove ? '' : obj.media ? "@media ".concat(obj.media, " {").concat(obj.css, "}") : obj.css; // For old IE

  /* istanbul ignore if  */

  if (style.styleSheet) {
    style.styleSheet.cssText = replaceText(index, css);
  } else {
    var cssNode = document.createTextNode(css);
    var childNodes = style.childNodes;

    if (childNodes[index]) {
      style.removeChild(childNodes[index]);
    }

    if (childNodes.length) {
      style.insertBefore(cssNode, childNodes[index]);
    } else {
      style.appendChild(cssNode);
    }
  }
}

function applyToTag(style, options, obj) {
  var css = obj.css;
  var media = obj.media;
  var sourceMap = obj.sourceMap;

  if (media) {
    style.setAttribute('media', media);
  } else {
    style.removeAttribute('media');
  }

  if (sourceMap && typeof btoa !== 'undefined') {
    css += "\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap)))), " */");
  } // For old IE

  /* istanbul ignore if  */


  if (style.styleSheet) {
    style.styleSheet.cssText = css;
  } else {
    while (style.firstChild) {
      style.removeChild(style.firstChild);
    }

    style.appendChild(document.createTextNode(css));
  }
}

var singleton = null;
var singletonCounter = 0;

function addStyle(obj, options) {
  var style;
  var update;
  var remove;

  if (options.singleton) {
    var styleIndex = singletonCounter++;
    style = singleton || (singleton = insertStyleElement(options));
    update = applyToSingletonTag.bind(null, style, styleIndex, false);
    remove = applyToSingletonTag.bind(null, style, styleIndex, true);
  } else {
    style = insertStyleElement(options);
    update = applyToTag.bind(null, style, options);

    remove = function remove() {
      removeStyleElement(style);
    };
  }

  update(obj);
  return function updateStyle(newObj) {
    if (newObj) {
      if (newObj.css === obj.css && newObj.media === obj.media && newObj.sourceMap === obj.sourceMap) {
        return;
      }

      update(obj = newObj);
    } else {
      remove();
    }
  };
}

module.exports = function (list, options) {
  options = options || {}; // Force single-tag solution on IE6-9, which has a hard limit on the # of <style>
  // tags it will allow on a page

  if (!options.singleton && typeof options.singleton !== 'boolean') {
    options.singleton = isOldIE();
  }

  list = list || [];
  var lastIdentifiers = modulesToDom(list, options);
  return function update(newList) {
    newList = newList || [];

    if (Object.prototype.toString.call(newList) !== '[object Array]') {
      return;
    }

    for (var i = 0; i < lastIdentifiers.length; i++) {
      var identifier = lastIdentifiers[i];
      var index = getIndexByIdentifier(identifier);
      stylesInDom[index].references--;
    }

    var newLastIdentifiers = modulesToDom(newList, options);

    for (var _i = 0; _i < lastIdentifiers.length; _i++) {
      var _identifier = lastIdentifiers[_i];

      var _index = getIndexByIdentifier(_identifier);

      if (stylesInDom[_index].references === 0) {
        stylesInDom[_index].updater();

        stylesInDom.splice(_index, 1);
      }
    }

    lastIdentifiers = newLastIdentifiers;
  };
};

/***/ }),

/***/ "./css/widget.css":
/*!************************!*\
  !*** ./css/widget.css ***!
  \************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var api = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
            var content = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./widget.css */ "./node_modules/css-loader/dist/cjs.js!./css/widget.css");

            content = content.__esModule ? content.default : content;

            if (typeof content === 'string') {
              content = [[module.id, content, '']];
            }

var options = {};

options.insert = "head";
options.singleton = false;

var update = api(content, options);



module.exports = content.locals || {};

/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"name":"parchords-jupyter","version":"0.1.0","description":"jupyter widget with parallel coords that enables interactive sonification","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/fhstp/parchords-jupyter","bugs":{"url":"https://github.com/fhstp/parchords-jupyter/issues"},"license":"MIT","author":{"name":"Alexander Rind","url":"https://github.com/alex-rind/"},"contributors":["Kajetan Enge","SoniVis project (https://research.fhstp.ac.at/en/projects/sonivis-data-analytics-using-sonification-and-visualization)"],"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/fhstp/parchords-jupyter"},"scripts":{"build":"npm run build:lib && npm run build:nbextension:dev && npm run build:labextension:dev","build:prod":"npm run build:lib && npm run build:nbextension && npm run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack --mode=production","build:nbextension:dev":"webpack --mode=development","clean":"npm run clean:lib && npm run clean:nbextension && npm run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf parchords_jupyter/labextension","clean:nbextension":"rimraf parchords_jupyter/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"npm run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2 || ^3 || ^4 || ^5 || ^6","d3-array":"^3.2.4","d3-axis":"^3.0.0","d3-scale":"^4.0.2","d3-scale-chromatic":"^3.0.0","d3-selection":"^3.0.0","d3-shape":"^3.2.0"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyter-widgets/base-manager":"^1.0.2","@jupyterlab/builder":"^3.0.0","@lumino/application":"^1.6.0","@lumino/widgets":"^1.6.0","@types/d3-array":"^3.0.7","@types/d3-axis":"^3.0.3","@types/d3-scale":"^4.0.4","@types/d3-scale-chromatic":"^3.0.0","@types/d3-selection":"^3.0.6","@types/d3-shape":"^3.1.2","@types/jest":"^26.0.0","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.61.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"parchords_jupyter/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_widget_js.5166c78270a04e55a91d.js.map