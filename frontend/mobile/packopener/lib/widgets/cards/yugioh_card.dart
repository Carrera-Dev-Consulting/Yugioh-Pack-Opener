import 'package:flutter/material.dart';
import 'package:packopener/models/cards/yugioh_card_model.dart';
import 'package:packopener/widgets/cards/backs/yugioh_card_back.dart';
import 'package:packopener/widgets/cards/front/yugioh_card_front.dart';
import '../base/playing_card.dart';

class YugiohCard extends PlayingCard {
  final YugiohCardModel? model;
  final VoidCallback? click;
  YugiohCard(
      {super.key,
      super.size = 1,
      super.back = const YugiohCardBack(),
      required this.model,
      this.click})
      : super(front: YugiohCardFront(model: model));
}
