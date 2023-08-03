import 'dart:convert';

import 'package:flutter/services.dart';

class JsonDummyReader {
  static Future<Map<String, dynamic>> readJson() async {
    final String response =
        await rootBundle.loadString("assets/data/yugioh.json");
    final data = await json.decode(response);
    return data;
  }
}
