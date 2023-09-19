// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
'use strict';

import { Panel } from '@lumino/widgets';

import type { CodeEditor } from '@jupyterlab/codeeditor';

import type { IRenderMimeRegistry } from '@jupyterlab/rendermime';

import { CellDiffWidget } from './cell';

import {
  CHUNK_PANEL_CLASS,
  ADDED_CHUNK_PANEL_CLASS,
  REMOVED_CHUNK_PANEL_CLASS,
} from './common';

import { MetadataDiffWidget } from './metadata';

import type { IDiffWidgetOptions } from '../../common/interfaces';

import type { NotebookDiffModel } from '../model';

const NBDIFF_CLASS = 'jp-Notebook-diff';

/**
 * NotebookDiffWidget
 */
export class NotebookDiffWidget extends Panel {
  constructor({
    editorFactory,
    model,
    rendermime,
  }: IDiffWidgetOptions<NotebookDiffModel>) {
    super();
    this._editorFactory = editorFactory;
    this._model = model;
    this._rendermime = rendermime;
    this.addClass(NBDIFF_CLASS);
  }

  /**
   * Start adding sub-widgets.
   *
   * Separated from constructor to allow 'live' adding of widgets
   */
  init(): Promise<void> {
    let model = this._model;
    let rendermime = this._rendermime;

    let work = Promise.resolve();
    work = work.then(() => {
      if (model.metadata) {
        this.addWidget(
          new MetadataDiffWidget({
            model: model.metadata,
            editorFactory: this._editorFactory,
          }),
        );
      }
    });
    for (let chunk of model.chunkedCells) {
      work = work.then(() => {
        return new Promise<void>(resolve => {
          if (chunk.length === 1 && !(chunk[0].added || chunk[0].deleted)) {
            this.addWidget(
              new CellDiffWidget({
                model: chunk[0],
                rendermime,
                mimetype: model.mimetype,
                editorFactory: this._editorFactory,
              }),
            );
          } else {
            let chunkPanel = new Panel();
            chunkPanel.addClass(CHUNK_PANEL_CLASS);
            let addedPanel = new Panel();
            addedPanel.addClass(ADDED_CHUNK_PANEL_CLASS);
            let removedPanel = new Panel();
            removedPanel.addClass(REMOVED_CHUNK_PANEL_CLASS);
            for (let cell of chunk) {
              let target = cell.deleted ? removedPanel : addedPanel;
              target.addWidget(
                new CellDiffWidget({
                  model: cell,
                  rendermime,
                  mimetype: model.mimetype,
                  editorFactory: this._editorFactory,
                }),
              );
            }
            chunkPanel.addWidget(addedPanel);
            chunkPanel.addWidget(removedPanel);
            this.addWidget(chunkPanel);
          }
          // This limits us to drawing 60 cells per second, which shouldn't
          // be a problem...
          requestAnimationFrame(() => {
            resolve();
          });
        });
      });
    }
    return work;
  }

  /**
   * Get the model for the widget.
   *
   * #### Notes
   * This is a read-only property.
   */
  get model(): NotebookDiffModel {
    return this._model;
  }

  private _editorFactory: CodeEditor.Factory | undefined;
  private _model: NotebookDiffModel;
  private _rendermime: IRenderMimeRegistry;
}
