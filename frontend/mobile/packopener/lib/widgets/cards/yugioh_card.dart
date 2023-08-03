import 'package:flutter/material.dart';
import 'package:packopener/models/cards/yugioh_card_model.dart';
import 'package:packopener/widgets/cards/backs/yugioh_card_back.dart';
import '../../constants.dart';
import '../../controllers/json_dummy_reader.dart';
import '../base/playing_card.dart';

class YugiohCard extends PlayingCard {
  final YugiohCardModel? model;

  const YugiohCard({super.key, this.model});

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<Map<String, dynamic>>(
        future: JsonDummyReader.readJson(),
        builder: (context, AsyncSnapshot<Map<String, dynamic>> snapshot) {
          if (snapshot.hasData) {
            var cardModel = YugiohCardModel.fromJson(snapshot.data!);
            return Container(
                width: YugiohConstants.CARD_WIDTH * size,
                height: YugiohConstants.CARD_HEIGHT * size,
                decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(4),
                    color: Colors.black),
                child: visible
                    ? Image.network(cardModel.image,
                        scale: size,
                        width: YugiohConstants.PICTURE_WIDTH,
                        height: YugiohConstants.PICTURE_HEIGHT)
                    : YugiohCardBack(size: size));
          } else {
            return YugiohCardBack(size: size);
          }
        });
  }
}
