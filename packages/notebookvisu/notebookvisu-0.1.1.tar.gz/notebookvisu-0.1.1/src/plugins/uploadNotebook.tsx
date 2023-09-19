import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import {
  PluginIDs,
  CommandIDs,
  notebookSelector,
  BACKEND_API_URL,
  Selectors
} from '../utils/constants';
import React from 'react';
import { IFileBrowserFactory } from '@jupyterlab/filebrowser';
import { fileUploadIcon } from '@jupyterlab/ui-components';
import { showDialog, Dialog } from '@jupyterlab/apputils';
import { IMainMenu } from '@jupyterlab/mainmenu';

const SuccessDialogContent = (props: { url: string; fileName: string }) => {
  return (
    <div>
      <p>Successfully uploaded, can be downloaded accessing:</p>
      <a href={props.url} target="_blank" style={{ textDecoration: 'none' }}>
        Download {props.fileName}
      </a>
    </div>
  );
};

function uploadNotebook(
  notebookContent: any,
  notebookName: string
): Promise<any> {
  return new Promise((resolve, reject) => {
    const formData = new FormData();
    formData.append('notebook_content', JSON.stringify(notebookContent));
    formData.append('name', notebookName);

    const url = BACKEND_API_URL + '/notebook/upload';
    fetch(url, {
      method: 'POST',
      body: formData
    })
      .then(response => {
        if (response.ok) {
          resolve(response.json()); // resolve the promise with the response data
        } else {
          reject(new Error('Failed to upload notebook on the backend')); // reject the promise with an error
        }
      })
      .catch(error => {
        console.log('Error occurred while uploading notebook:', error);
        reject(error);
      });
  });
}

function activateUpload(
  app: JupyterFrontEnd,
  factory: IFileBrowserFactory,
  mainMenu: IMainMenu
) {
  console.log('JupyterLab extension upload is activated!');

  app.commands.addCommand(CommandIDs.uploadNotebook, {
    label: 'Upload notebook for dashboard tracking',
    icon: args => (args['isContextMenu'] ? fileUploadIcon : undefined),
    execute: args => {
      const file = factory.tracker.currentWidget?.selectedItems().next().value;

      if (file) {
        app.serviceManager.contents.get(file.path).then(getResponse => {
          uploadNotebook(getResponse.content, file.name)
            .then(uploadResponse => {
              // shallow copy and changing the content with the upgraded returned notebook
              const contentToSave = {
                ...getResponse,
                content: uploadResponse
              };
              app.serviceManager.contents
                .save(file.path, contentToSave)
                .then(saveResponse => {
                  const notebookId =
                    uploadResponse['metadata'][Selectors.notebookId];
                  const url = `${BACKEND_API_URL}/notebook/download/${notebookId}`;
                  showDialog({
                    title: file.name,
                    body: (
                      <SuccessDialogContent url={url} fileName={file.name} />
                    ),
                    buttons: [Dialog.okButton()]
                  }).catch(e => console.log(e));
                });
            })
            .catch(e => {
              showDialog({
                title: file.name,
                body: 'Error uploading the file',
                buttons: [Dialog.cancelButton()]
              }).catch(e => console.log(e));
            });
        });
      }
    }
  });

  app.contextMenu.addItem({
    selector: notebookSelector,
    type: 'separator',
    rank: 0
  });
  app.contextMenu.addItem({
    args: { isContextMenu: true },
    command: CommandIDs.uploadNotebook,
    selector: notebookSelector,
    rank: 0
  });
  app.contextMenu.addItem({
    selector: notebookSelector,
    type: 'separator',
    rank: 0
  });
}

const uploadNotebookPlugin: JupyterFrontEndPlugin<void> = {
  id: PluginIDs.uploadNotebookPlugin,
  autoStart: true,
  requires: [IFileBrowserFactory, IMainMenu],
  activate: activateUpload
};

export default uploadNotebookPlugin;
