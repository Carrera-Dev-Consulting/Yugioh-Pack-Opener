import '../enums/game.dart';

abstract class CardModel {
  final String description;
  final String type;
  final String name;
  final List<String> images;
  final Game game;
  const CardModel(
      {required this.name,
      required this.description,
      required this.type,
      required this.game,
      required this.images});
}
