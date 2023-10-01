// This file is part of Invenio.
//
// Copyright (C) 2023 Graz University of Technology.
//
// invenio-records-dublin-core is free software; you can redistribute it and/or
// modify it under the terms of the MIT License; see LICENSE file for more
// details.

import { parametrize } from "react-overridable";
import { createSearchAppInit } from "@js/invenio_search_ui";
import {
  RDMRecordSearchBarContainer,
  RDMToggleComponent,
  RDMCountComponent,
  RDMErrorComponent,
  RDMEmptyResults,
} from "@js/invenio_app_rdm/search/components";
import {
  ContribSearchAppFacets,
  ContribBucketAggregationElement,
  ContribBucketAggregationValuesElement,
} from "@js/invenio_search_ui/components";
import {
  DublinCoreRecordResultsGridItem,
  DublinCoreRecordResultsListItem,
} from "./components";

const appName = "DublinCoreRecords.Search";

const ContribSearchAppFacetsWithConfig = parametrize(ContribSearchAppFacets, {
  toggle: true,
});

const RDMRecordSearchBarContainerWithConfig = parametrize(
  RDMRecordSearchBarContainer,
  {
    appName: appName,
  }
);

const initSearchApp = createSearchAppInit({
  "BucketAggregation.element": ContribBucketAggregationElement,
  "BucketAggregationValues.element": ContribBucketAggregationValuesElement,
  //"EmptyResults.element": RDMEmptyResults,
  "ResultsGrid.item": DublinCoreRecordResultsGridItem,
  "ResultsList.item": DublinCoreRecordResultsListItem,
  "SearchApp.facets": ContribSearchAppFacetsWithConfig,
  "SearchApp.searchbarContainer": RDMRecordSearchBarContainerWithConfig,
  "SearchFilters.ToggleComponent": RDMToggleComponent,
  //"Error.element": RDMErrorComponent,
  "Count.element": RDMCountComponent,
  //"SearchFilters.Toggle.element": RDMToggleComponent,
});