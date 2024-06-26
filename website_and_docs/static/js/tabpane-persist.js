// Storage key names and data attribute name:
const td_persistStorageKeyNameBase = 'td-tp-persist';
const td_persistCounterStorageKeyName = `${td_persistStorageKeyNameBase}-count`;
const td_persistDataAttrName = `data-${td_persistStorageKeyNameBase}`;

// Utilities

const _tdPersistCssSelector = (attrValue) =>
  attrValue
    ? `[${td_persistDataAttrName}="${attrValue}"]`
    : `[${td_persistDataAttrName}]`;

const _tdStoragePersistKey = (tabKey) =>
  td_persistStorageKeyNameBase + ':' + (tabKey || '');

const _tdSupportsLocalStorage = () => typeof Storage !== 'undefined';

// Helpers

function tdPersistKey(key, value) {
  // @requires: tdSupportsLocalStorage();

  try {
    if (value) {
      localStorage.setItem(key, value);
    } else {
      localStorage.removeItem(key);
    }
  } catch (error) {
    const action = value ? 'add' : 'remove';
    console.error(
      `Docsy tabpane: unable to ${action} localStorage key '${key}': `,
      error
    );
  }
}

function getActiveTabFromURL() {
  const urlParams = new URLSearchParams(window.location.search);
  const activeTab = urlParams.get('tab');
  return activeTab ? activeTab.toLowerCase() : null;
}

function adjustTabContentHeights() {
  const contentTabs = document.querySelectorAll('.tab-content');

  // Loop through each tabpane
  contentTabs.forEach(contentTab => {
    let maxHeight = 0;
    const tabPanes = contentTab.querySelectorAll('.tab-pane');

    // Loop through each tab in the tabpanes list to find max
    tabPanes.forEach(tab => {
      tab.style.display = 'block';
      maxHeight = Math.max(maxHeight, tab.clientHeight);
      tab.style.display = '';
    });

    // Loop through each tab in the tabpanes list to set height
    tabPanes.forEach(tab => {
      tab.style.height = maxHeight + 'px';
    });
  });
}

// Retrieve, increment, and store tab-select event count, then returns it.
function tdGetTabSelectEventCountAndInc() {
  // @requires: tdSupportsLocalStorage();

  const storedCount = localStorage.getItem(td_persistCounterStorageKeyName);
  let numTabSelectEvents = parseInt(storedCount) || 0;
  numTabSelectEvents++;
  tdPersistKey(td_persistCounterStorageKeyName, numTabSelectEvents.toString());
  return numTabSelectEvents;
}

// Main functions

function tdActivateTabsWithKey(key) {
  if (!key) return;

  document.querySelectorAll(_tdPersistCssSelector(key)).forEach((element) => {
    new bootstrap.Tab(element).show();
  });
}

function tdPersistActiveTab(activeTabKey) {
  if (!_tdSupportsLocalStorage()) return;

  tdPersistKey(
    _tdStoragePersistKey(activeTabKey),
    tdGetTabSelectEventCountAndInc()
  );
  tdActivateTabsWithKey(activeTabKey);
}

// Handlers

function tdGetAndActivatePersistedTabs(tabs) {
  // Get unique persistence keys of tabs in this page
  var keyOfTabsInThisPage = [
    ...new Set(
      Array.from(tabs).map((el) => el.getAttribute(td_persistDataAttrName))
    ),
  ];

  // Create a list of active tabs with their age:
  let key_ageList = keyOfTabsInThisPage
    // Map to [tab-key, last-activated-age]
    .map((k) => [
      k,
      parseInt(localStorage.getItem(_tdStoragePersistKey(k))) || 0,
    ])
    // Exclude tabs that have never been activated
    .filter(([k, v]) => v)
    // Sort from oldest selected to most recently selected
    .sort((a, b) => a[1] - b[1]);

  // Activate tabs from the oldest to the newest
  key_ageList.forEach(([key]) => {
    tdActivateTabsWithKey(key);
  });

  return key_ageList;
}

function tdRegisterTabClickHandler(tabs) {
  tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      const activeTabKey = tab.getAttribute(td_persistDataAttrName);
      tdPersistActiveTab(activeTabKey);
    });
  });
}

// Register listeners and activate tabs

window.addEventListener('DOMContentLoaded', () => {
  if (!_tdSupportsLocalStorage()) return;

  var allTabsInThisPage = document.querySelectorAll(_tdPersistCssSelector());
  tdRegisterTabClickHandler(allTabsInThisPage);

  const activeTabKeyFromURL = getActiveTabFromURL();
  if (activeTabKeyFromURL) {
    tdActivateTabsWithKey(activeTabKeyFromURL);
  } else {
    tdGetAndActivatePersistedTabs(allTabsInThisPage);
  }
  // Adjust tab content heights
  adjustTabContentHeights();
});
