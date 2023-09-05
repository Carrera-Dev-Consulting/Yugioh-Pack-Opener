import 'package:flutter_test/flutter_test.dart';
import 'package:packopener/pages/home_page.dart';

void main() {
  testWidgets("Shop button exists on the Home page", (tester) async {
    await tester.pumpWidget(const MyHomePage());
    expect(find.text("Shop"), findsOneWidget);
  });
}
