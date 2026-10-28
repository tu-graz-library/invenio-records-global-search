/*
 * SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
 * SPDX-License-Identifier: MIT
 */

import React, { useState } from "react";
import { Card, Icon } from "semantic-ui-react";

export const GlobalSearchBucketAggregationElement = ({
  title,
  containerCmp,
}) => {
  const [active, setActive] = useState(true);

  return (
    <Card className="borderless facet">
      <Card.Content>
        <Card.Header
          as="h2"
          style={{ float: "left", minHeight: 0, cursor: "pointer" }}
          onClick={() => setActive((active) => !active)}
        >
          <Icon
            style={{ "margin-top": "-4px" }}
            name={active ? "angle down" : "angle right"}
          />
          {title}
        </Card.Header>
        {active ? containerCmp : null}
      </Card.Content>
    </Card>
  );
};
