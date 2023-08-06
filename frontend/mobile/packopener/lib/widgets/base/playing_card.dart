import 'package:flutter/widgets.dart';

abstract class PlayingCard extends StatelessWidget {
  final double size;
  bool visible;

  PlayingCard({super.key, this.size = 1, this.visible = false});

  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
