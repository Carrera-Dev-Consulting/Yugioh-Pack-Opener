import 'package:packopener/models/cards/yugioh_card_model.dart';
import 'package:packopener/models/enums/game.dart';
import 'package:packopener/widgets/base/card_front.dart';

class YugiohCardFront extends CardFront {
  final YugiohCardModel? model;
  YugiohCardFront({super.key, required this.model, super.size = 1})
      : super(card: model!, game: Game.yugioh);
}
