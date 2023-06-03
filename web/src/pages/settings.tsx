import { useI18n } from "@solid-primitives/i18n";
import Button from "../ui/Button";
import Flex from "../ui/Flex";

export default function Page() {
  const [t] = useI18n();
  
  function loadGame() {
  }
  
  function saveGame() {
    alert(t("settings.saves.save_ok"));
  }

  return <>
    <Flex>
      <h1>{t("settings.title")}</h1>
    </Flex>
    <h2>{t("settings.saves.title")}</h2>
    <Flex>
      <Button onClick={loadGame}>{t("settings.saves.load")}</Button>
      <Button onClick={saveGame}>{t("settings.saves.save")}</Button>
    </Flex>

  </>
}