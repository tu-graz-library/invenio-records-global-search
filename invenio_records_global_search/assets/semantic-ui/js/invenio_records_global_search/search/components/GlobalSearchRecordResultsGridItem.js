/*
 * SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
 * SPDX-License-Identifier: MIT
 */

import React from "react";
import { get, truncate } from "lodash";
import { Card } from "semantic-ui-react";

export const GlobalSearchRecordResultsGridItem = ({ result, index }) => {
  const metadata = get(result, ["ui", "metadata", "json"], []);
  const description = get(
    metadata,
    ["summary", "0", "summary"],
    "No description"
  );
  return (
    <Card fluid key={index} href={`/global-search/${result.pid}`}>
      <Card.Content>
        <Card.Header>{result.metadata.json.title_statement.title}</Card.Header>
        <Card.Description>
          {truncate(description, { length: 200 })}
        </Card.Description>
      </Card.Content>
    </Card>
  );
};
