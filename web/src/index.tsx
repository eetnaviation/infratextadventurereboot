/* @refresh reload */
import { render } from 'solid-js/web';
import { I18nContext, createI18nContext, useI18n } from '@solid-primitives/i18n';
import { Route, Router, Routes } from '@solidjs/router';
import { lazy } from "solid-js";

import { lang_en } from './lang/en';

import "./css/index.css";


render(() => {
  const lang = createI18nContext({
    en: lang_en,
  }, "en");

  return <>
    <I18nContext.Provider value={lang}>
      <Router>
        <App />
      </Router>
    </I18nContext.Provider>
  </>
}, document.getElementById('root')!);

function App() {
  //const [t] = useI18n();

  return <>
    <div class="main">
      <div class="content">
        <Routes>
          <Route path="/game" component={lazy(() => import("./pages/game"))} />
          <Route path="/settings" component={lazy(() => import("./pages/settings"))} />
        </Routes>
      </div>
    </div>
  </>
}