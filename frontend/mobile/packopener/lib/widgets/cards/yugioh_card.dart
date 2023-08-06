import 'package:flutter/material.dart';
import 'package:packopener/controllers/yugioh_data_reader.dart';
import 'package:packopener/models/cards/yugioh_card_model.dart';
import 'package:packopener/widgets/cards/backs/yugioh_card_back.dart';
import 'package:packopener/widgets/cards/yugioh_card_front.dart';
import '../../constants.dart';
import '../../models/dto/yugioh_card_dto.dart';
import '../base/playing_card.dart';

class YugiohCard extends PlayingCard {
  final YugiohCardModel? model;
  final VoidCallback? click;
  YugiohCard(
      {super.key,
      super.size = 1,
      super.visible = false,
      this.model,
      required this.click});

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<YugiohCardDTO>>(
        future: YugiohDataReader.readJson(),
        builder: (context, AsyncSnapshot<List<YugiohCardDTO>> snapshot) {
          if (snapshot.hasData) {
            var cardModels = YugiohCardModel.fromDTO(snapshot.data![1]);
            return InkWell(
                onTap: click,
                child: Container(
                    width: YugiohConstants.CARD_WIDTH * size,
                    height: YugiohConstants.CARD_HEIGHT * size,
                    decoration:
                        BoxDecoration(borderRadius: BorderRadius.circular(4)),
                    child: !visible
                        ? YugiohCardFront(
                            model: cardModels,
                            size: size,
                          )
                        : YugiohCardBack(size: size)));
          } else {
            return YugiohCardBack(size: size);
          }
        });
  }
}
