import 'package:flutter/material.dart';
import 'package:packopener/widgets/cards/yugioh_card.dart';

import '../controllers/yugioh_data_reader.dart';
import '../models/cards/yugioh_card_model.dart';
import '../models/dto/yugioh_card_dto.dart';

class CardPage extends StatefulWidget {
  const CardPage({super.key});

  @override
  State<CardPage> createState() => _CardPageState();
}

class _CardPageState extends State<CardPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Center(
            //This reads a json file that is used for testing for now. Will be replaced with the api
            child: FutureBuilder<List<YugiohCardDTO>>(
                future: YugiohDataReader.readJson(),
                builder:
                    (context, AsyncSnapshot<List<YugiohCardDTO>> snapshot) {
                  if (snapshot.hasData) {
                    var cardModels = YugiohCardModel.fromDTO(snapshot.data![1]);
                    return YugiohCard(model: cardModels);
                  }
                  return Container();
                })));
  }
}
