import 'package:packopener/models/cards/card_model.dart';
import 'package:packopener/models/enums/game.dart';

class YugiohCardModel extends CardModel {
  final int level;
  final String attribute;
  final int attack;
  final int defense;
  final int cardNumber;

  YugiohCardModel(
      {required super.name,
      required super.description,
      required super.type,
      super.game = Game.yugioh,
      required super.image,
      required this.level,
      required this.attribute,
      required this.attack,
      required this.defense,
      required this.cardNumber});

  factory YugiohCardModel.fromJson(Map<String, dynamic> json) {
    return YugiohCardModel(
        level: json["level"],
        attribute: json["attribute"],
        attack: json["attack"],
        defense: json["defense"],
        cardNumber: json["cardNumber"],
        name: json["name"],
        description: json["description"],
        type: json["type"],
        image: json["image"]);
  }
}
