import 'package:flutter/material.dart';
import 'package:packopener/models/cards/yugioh_card_model.dart';
import '../../constants.dart';
import '../base/playing_card.dart';

class YugiohCardFront extends PlayingCard {
  final YugiohCardModel? model;
  YugiohCardFront({super.key, super.size = 1, required this.model});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: size * YugiohConstants.CARD_WIDTH,
        height: size * YugiohConstants.CARD_HEIGHT,
        child: Image.network(model!.images[0]));
  }
}
