export default interface PositionButton {
  readonly id: string;
  readonly onClick: () => void;
  readonly isVisible?: () => boolean;
}