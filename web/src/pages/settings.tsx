import { useI18n } from "@solid-primitives/i18n";
import Button from "../ui/Button";
import Flex from "../ui/Flex";

export default function Page() {
  const [t] = useI18n();
  
  function resetSave() {
    localStorage.clear();
    window.location.reload();
  }

  return <>
    <Flex>
      <h1>{t("settings.title")}</h1>
    </Flex>
    <h2>{t("settings.saves.title")}</h2>
    <Flex>
      <Button onClick={resetSave}>{t("settings.saves.reset")}</Button>
    </Flex>

  </>
}