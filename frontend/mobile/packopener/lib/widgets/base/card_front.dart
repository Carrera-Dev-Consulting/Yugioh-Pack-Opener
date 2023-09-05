import 'package:flutter/material.dart';
import 'package:packopener/models/cards/card_model.dart';
import '../../constants.dart';

abstract class CardFront extends StatelessWidget {
  final CardModel card;
  final int size;
  const CardFront({super.key, this.size = 1, required this.card});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: size * BaseCard.CARD_WIDTH,
        height: size * BaseCard.CARD_HEIGHT,
        child: Image.network(card.images[0]));
  }
}
