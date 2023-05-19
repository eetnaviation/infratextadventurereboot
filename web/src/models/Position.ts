import PositionButton from "./PositionButton";

export default interface Position {
  readonly id: string;
  readonly buttons: PositionButton[];
  readonly onEnter?: () => void;
  readonly onLeave?: () => void;
}