// Copyright (c) Alexander Rind & the SoniVis team.
// Distributed under the terms of the MIT License (see LICENSE).

import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import { MODULE_NAME, MODULE_VERSION } from './version';

// Import the CSS
import '../css/widget.css';
import { ParChords } from './parchords';

export class ParChordsModel extends DOMWidgetModel {
  defaults(): any {
    return {
      ...super.defaults(),
      _model_name: ParChordsModel.model_name,
      _model_module: ParChordsModel.model_module,
      _model_module_version: ParChordsModel.model_module_version,
      _view_name: ParChordsModel.view_name,
      _view_module: ParChordsModel.view_module,
      _view_module_version: ParChordsModel.view_module_version,

      axis_fields: [] as string[],
      color_field: '',
      _marks_val: [] as number[][],
      _marks_color: [] as number[],
      width: 700,
      height: 400,
    };
  }

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
    // Add any extra serializers here
  };

  static model_name = 'ParChordsModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'ParChordsView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class ParChordsView extends DOMWidgetView {
  render(): void {
    new ParChords(this);
  }
}
