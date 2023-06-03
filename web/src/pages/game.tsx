import { For, onMount } from "solid-js";
import Flex from "../ui/Flex";
import Game from "../models/Game";
import Button from "../ui/Button";
import { useI18n } from "@solid-primitives/i18n";

export default function Page() {
  const [t] = useI18n();
  const state = Game.state;

  onMount(() => {
    Game.init();
  });

  return <>
    <div class="text">
      {t(`${state.level?.id}.${state.position?.id}.text`)}
    </div>

    <div class="buttons">
      <Flex direction="column">
        <For each={state.position?.buttons}>
          {(button) => <>
            <Button>{t(`${state.level?.id}.${state.position?.id}.button.${button.id}`)}</Button>
          </>}
        </For>
      </Flex>
    </div>
  </>
}