import Position from "./Position";

export default interface Level<LevelData> {
  readonly id: string;
  readonly saveData: LevelData;
  readonly defaultPosition: string;
  readonly positions: Position[];
  readonly onEnter?: () => void;
  readonly onLeave?: () => void;
  readonly onChangePosition?: () => void;
}