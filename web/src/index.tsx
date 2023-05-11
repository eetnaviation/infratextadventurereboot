/* @refresh reload */
import { render } from 'solid-js/web';

import "./css/index.css";

render(() => <App />, document.getElementById('root')!);

function App() {

  return <>
      <div class="main">
        <div class="content">
          <div class="text">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis velit sit quos necessitatibus a. Laborum numquam cum explicabo velit fuga voluptates ducimus, qui dolorum sint a et recusandae natus harum.
            Nostrum doloremque saepe, sapiente labore, illum soluta illo aliquam excepturi unde eos velit nihil accusamus. Minus animi, totam tenetur quos molestiae fuga eum assumenda ducimus dignissimos doloremque minima quasi eveniet.
            Consequatur id excepturi repudiandae molestiae, ab modi enim voluptate? Porro beatae esse quam minus, quis delectus sint recusandae consequuntur eaque sit, eligendi iure, qui distinctio odit obcaecati id quod incidunt.
          </div>

          <div class="buttons">
            <button class="button">Lorem ipsum dolor sit amet consectetur adipisicing elit.</button>
            <button class="button">Lorem ipsum dolor sit amet consectetur adipisicing elit.</button>
            <button class="button">Lorem ipsum dolor sit amet consectetur adipisicing elit.</button>
          </div>
        </div>

      </div>
  </>
}