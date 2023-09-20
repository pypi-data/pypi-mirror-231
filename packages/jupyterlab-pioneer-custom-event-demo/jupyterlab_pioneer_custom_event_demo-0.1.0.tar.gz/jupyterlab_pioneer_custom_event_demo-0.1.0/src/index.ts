import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { NotebookPanel, INotebookTracker } from '@jupyterlab/notebook';
import { Widget } from '@lumino/widgets';
import { IJupyterLabPioneer } from 'jupyterlab-pioneer';

const PLUGIN_ID = 'jupyterlab-pioneer-custom-event-demo:plugin';

const plugin: JupyterFrontEndPlugin<void> = {
  id: PLUGIN_ID,
  description:
    'A JupyterLab extension that generates telemetry data when users click on a button.',
  autoStart: true,
  requires: [IJupyterLabPioneer, INotebookTracker],
  activate: async (
    app: JupyterFrontEnd,
    pioneer: IJupyterLabPioneer,
    notebookTracker: INotebookTracker
  ) => {
    console.log(`${PLUGIN_ID}`);

    const button = document.createElement('button');
    const buttonText = document.createTextNode('Click me');
    button.appendChild(buttonText);
    button.id = 'jupyterlab-pioneer-custom-event-demo-button';

    const node = document.createElement('div');
    node.appendChild(button);

    notebookTracker.widgetAdded.connect(
      async (_, notebookPanel: NotebookPanel) => {
        notebookPanel.toolbar.insertAfter(
          'restart-and-run',
          'telemetry-producer-demo-button',
          new Widget({ node: node })
        );

        await notebookPanel.sessionContext.ready; // wait until session id is created
        await pioneer.router.loadNotebookPanel(notebookPanel);

        node.addEventListener('click', async () => {
          const event = {
            eventName: 'ClickButtonEvent',
            eventTime: Date.now()
          };
          await pioneer.router.publishEvent(event, true);
          window.alert('Telemetry data sent');
        });
      }
    );
  }
};

export default plugin;
