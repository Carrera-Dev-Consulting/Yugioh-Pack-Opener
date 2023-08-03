import 'package:flutter/widgets.dart';

import '../../constants.dart';

abstract class CardBack extends StatelessWidget {
  final double size;
  final String image;
  final double width;
  final double height;
  const CardBack(
      {super.key,
      this.size = 1,
      required this.image,
      required this.width,
      required this.height});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: YugiohConstants.CARD_WIDTH,
      height: YugiohConstants.CARD_HEIGHT,
      child: Image.network(
        image,
        width: YugiohConstants.CARD_WIDTH * size,
        height: YugiohConstants.CARD_HEIGHT * size,
      ),
    );
  }
}
