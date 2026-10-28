/*
 * SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
 * SPDX-License-Identifier: MIT
 */

import { parametrize } from "react-overridable";
import { createSearchAppInit } from "@js/invenio_search_ui";
import {
  RDMRecordSearchBarContainer,
  RDMRecordMultipleSearchBarElement,
  RDMToggleComponent,
  RDMCountComponent,
  RDMErrorComponent,
  RDMEmptyResults,
} from "@js/invenio_app_rdm/search/components";
import {
  ContribSearchAppFacets,
  ContribBucketAggregationValuesElement,
} from "@js/invenio_search_ui/components";
import {
  // GlobalSearchRecordResultsGridItem,
  GlobalSearchRecordResultsListItem,
  GlobalSearchEmptyResults,
  GlobalSearchBucketAggregationElement,
} from "./components";

const appName = "GlobalSearchRecords.Search";

const ContribSearchAppFacetsWithConfig = parametrize(ContribSearchAppFacets, {
  toggle: false,
});

const RDMRecordSearchBarContainerWithConfig = parametrize(
  RDMRecordSearchBarContainer,
  {
    appName: appName,
  }
);

const initSearchApp = createSearchAppInit({
  "BucketAggregation.element": GlobalSearchBucketAggregationElement,
  "BucketAggregationValues.element": ContribBucketAggregationValuesElement,
  "EmptyResults.element": GlobalSearchEmptyResults,
  // "ResultsGrid.item": GlobalSearchRecordResultsGridItem,
  "ResultsList.item": GlobalSearchRecordResultsListItem,
  "SearchApp.facets": ContribSearchAppFacetsWithConfig,
  "SearchApp.searchbarContainer": RDMRecordSearchBarContainerWithConfig,
  "SearchBar.element": RDMRecordMultipleSearchBarElement,
  "SearchFilters.ToggleComponent": RDMToggleComponent,
  // "Error.element": RDMErrorComponent,
  "Count.element": RDMCountComponent,
});
