// This file is part of Invenio.
//
// Copyright (C) 2023 Graz University of Technology.
//
// invenio-records-dublin-core is free software; you can redistribute it and/or
// modify it under the terms of the MIT License; see LICENSE file for more
// details.

import React, { useState } from "react";
import { truncate, get } from "lodash";
import { Button, Item, Label } from "semantic-ui-react";
import { i18next } from "../../../../translations/invenio_records_dublin_core/i18next";

export const DublinCoreRecordResultsListItem = ({ result, index }) => {
  const version = get(result, "revision_id", null);

  const publishedAt = "TODO";
  const publicationDate = "TODO";
  const createdDate = "TODO";

  const titles = [get(result, "metadata.title", "No titles")];

  const accessId = "TODO";
  const accessIcon = "TODO";
  const accessStatus = "TODO";

  const resourceType = "TODO";
  const description = "TODO";
  const subjects = ["TODO"];

  const creators = ["TODO"];

  const viewLink = get(result, "metadata.original_link");

  const [error, setError] = useState("");

  const handleError = (errorMessage) => {
    setError(errorMessage);
  };

  return (
    <Item key={index}>
      <Item.Content>
        <Item.Extra>
          <div>
            <Label size="tiny" color="blue">
              {publishedAt ? `${publishedAt}` : publicationDate}
              {version ? `(${version})` : null}
            </Label>
            <Label size="tiny" className={`access-status ${accessId}`}>
              {accessIcon && <i className={`icon ${accessIcon}`}></i>}
              {accessStatus}
            </Label>
            {resourceType && (
              <Label size="tiny" color="blue">
                {resourceType}
              </Label>
            )}
            <Button
              basic
              compact
              size="small"
              floated="right"
              icon="eye"
              content={i18next.t("View")}
              href={viewLink}
            />
          </div>
        </Item.Extra>
        <Item.Header href={viewLink}>
          {titles.map((title) => (
            <span>{title}</span>
          ))}
        </Item.Header>
        <Item.Meta>
          {creators.map((creator, index) => (
            <span key={index}>
              {creator.a}
              {index < creators.length - 1 && ","}
            </span>
          ))}
        </Item.Meta>
        <Item.Description>
          {truncate(description, { length: 350 })}
        </Item.Description>
        <Item.Extra>
          {subjects.map((subject, index) => (
            <Label key={index} size="tiny">
              {subject.miscellaneous_information}
            </Label>
          ))}
          {createdDate && (
            <div>
              <small>
                {i18next.t("Uploaded on")}
                <span>{createdDate}</span>
              </small>
            </div>
          )}
        </Item.Extra>
      </Item.Content>
    </Item>
  );
};
