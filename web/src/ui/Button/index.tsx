import { JSXElement, children } from "solid-js";
import { Component } from "solid-js/types/render/component"
import "./index.css";

const Button: Component<{
  children: JSXElement;
  disabled?: boolean;
  onClick?: () => void;
}> = (props) => {
  const child = children(() => props.children);

  return <>
    <button
      classList={{
        "button": true,
        "button-disabled": props.disabled,
      }}
      onClick={props.onClick}
    >{child()}</button>
  </>
}

export default Button;