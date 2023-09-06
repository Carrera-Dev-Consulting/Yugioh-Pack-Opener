import 'package:flutter/material.dart';
import 'package:packopener/controllers/yugioh_data_reader.dart';
import 'package:packopener/models/cards/yugioh_card_model.dart';
import 'package:packopener/pages/card_page.dart';
import 'package:packopener/widgets/cards/yugioh_card.dart';
import 'package:packopener/widgets/packs/constants.dart';

abstract class Pack extends StatefulWidget {
  final int size;
  const Pack({super.key, this.size = 1});

  @override
  // ignore: library_private_types_in_public_api
  _ExpandedState createState() => _ExpandedState();
}

class _ExpandedState extends State<Pack> {
  double width = 200;
  double height = 500;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () async {
        var data =
            YugiohCardModel.translateModels(await YugiohDataReader.readJson())
                .map((e) => YugiohCard(model: e))
                .toList();
        setState(() {
          Navigator.of(context).push(
              MaterialPageRoute(builder: (context) => CardPage(cards: data)));
        });
      },
      child: SizedBox(
        width: width,
        height: height,
        child: Image.network(
          PackConstants.BACKGROUND,
          width: width * widget.size,
          height: height * widget.size,
        ),
      ),
    );
  }
}
