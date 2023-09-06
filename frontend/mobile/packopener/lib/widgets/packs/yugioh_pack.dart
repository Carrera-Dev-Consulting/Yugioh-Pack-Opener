import 'package:flutter/material.dart';
import 'package:packopener/widgets/base/pack.dart';
import 'package:packopener/widgets/packs/constants.dart';

class YugiohPack extends Pack {
  const YugiohPack({super.key, super.size = 1});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
        child: Image.network(PackConstants.BACKGROUND));
  }
}
