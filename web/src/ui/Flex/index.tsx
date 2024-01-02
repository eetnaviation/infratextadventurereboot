import { JSXElement, children } from "solid-js";
import { Component } from "solid-js/types/render/component"
import "./index.css";

const Flex: Component<{
  children: JSXElement;
  direction?: "column" | "row";
}> = (props) => {
  const child = children(() => props.children);

  return <>
    <div
      classList={{
        "flex": true,
        "flex-column": props.direction == "column",
        "flex-row": props.direction == "row",
      }}
    >{child()}</div>
  </>
}

export default Flex;