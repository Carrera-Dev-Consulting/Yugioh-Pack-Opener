import 'package:packopener/models/cards/card_model.dart';
import 'package:packopener/models/dto/yugioh_card_dto.dart';
import 'package:packopener/models/enums/game.dart';

class YugiohCardModel extends CardModel {
  final int level;
  final String attribute;
  final int attack;
  final int defense;

  YugiohCardModel({
    required super.name,
    required super.description,
    required super.type,
    super.game = Game.yugioh,
    required super.images,
    required this.level,
    required this.attribute,
    required this.attack,
    required this.defense,
  });

  factory YugiohCardModel.fromDTO(YugiohCardDTO dto) {
    return YugiohCardModel(
        level: dto.level,
        attribute: dto.attribute,
        attack: dto.attack,
        defense: dto.defense,
        name: dto.name,
        description: dto.description,
        type: dto.type,
        images: dto.images);
  }
}
