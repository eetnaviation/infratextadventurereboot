/* @refresh reload */
import { For, render } from 'solid-js/web';
import { I18nContext, createI18nContext, useI18n } from '@solid-primitives/i18n';
import PositionButton from './models/PositionButton';
import Game from './models/Game';

import { lang_en } from './lang/en';

import "./css/index.css";
import Button from './ui/Button';
import Flex from './ui/Flex';

render(() => {
  const lang = createI18nContext({
    en: lang_en,
  }, "en");

  return <>
    <I18nContext.Provider value={lang}>
      <App />
    </I18nContext.Provider>
  </>
}, document.getElementById('root')!);

function App() {
  const [t] = useI18n();

  return <>
    <div class="main">
      <div class="content">
        <div class="text">
          {Game.data.position?.id}
        </div>

        <Flex direction="column">
          <For each={Game.data.position?.buttons || []}>
            {(button: PositionButton) => {
              if ((button.isVisible != undefined && button.isVisible()) || button.isVisible == undefined) return <>
                <Button onClick={button.onClick}>
                  {t(`${Game.data.level.id}.${Game.data.position.id}.button.${button.id}`)}
                </Button>
              </>
            }}
          </For>
        </Flex>
      </div>
    </div>
  </>
}