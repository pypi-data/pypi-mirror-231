export const BACKEND_API_URL = 'https://unianalytics.ch/send/';
// export const BACKEND_API_URL = 'http://localhost:5000/send/';

export const PLUGIN_ID = 'send-3-test';

export const MAX_PAYLOAD_SIZE = 1048576; // 1*1024*1024 => 1Mb

export const POST_TOKEN = 'bac5ef8565dr480bagc6eef218673ad4';

// notebook metadata field names
const SELECTOR_ID = 'unianalytics';
export namespace Selectors {
  export const notebookId = `${SELECTOR_ID}_notebook_id`;

  export const instanceId = `${SELECTOR_ID}_instance_id`;

  export const cellMapping = `${SELECTOR_ID}_cell_mapping`;
}
