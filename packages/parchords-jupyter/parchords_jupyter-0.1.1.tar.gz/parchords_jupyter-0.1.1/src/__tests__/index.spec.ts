// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

// Add any needed widget imports here (or from controls)
// import {} from '@jupyter-widgets/base';

import { createTestModel } from './utils';

import { ParChordsModel } from '..';

describe('ParChordsWidget', () => {
  describe('ParChordsModel', () => {
    it('should be createable', () => {
      const model = createTestModel(ParChordsModel);
      expect(model).toBeInstanceOf(ParChordsModel);
      expect(model.get('color_field')).toEqual('');
    });

    // it('should be createable with a value', () => {
    //   const state = { value: 'Foo Bar!' };
    //   const model = createTestModel(ParChordsModel, state);
    //   expect(model).toBeInstanceOf(ParChordsModel);
    //   expect(model.get('value')).toEqual('Foo Bar!');
    // });
  });
});
