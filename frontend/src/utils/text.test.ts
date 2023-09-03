import { shortenText, InvalidOperation } from "./text";

describe("Testing shortenText", function () {
    test("Text that is less then max_length is returned as is", () => {
        const input = 'Some Simple text'
        const output = shortenText(input, input.length + 10)
        expect(output).toEqual(input)
    })
    test('Text that is greater then max_length is returned shortend with ellipsis', () => {
        const input = 'Throw us under the bus'
        const expected_output = 'Throw us...'
        const output = shortenText(input, expected_output.length)

        expect(output).toEqual(expected_output)
    })

    test('when given max_length less then 3 throws InvalidOperation error', () => {
        const scenario = () => {
            shortenText('Some input it doesn\'t matter', 1)
        }
        expect(scenario).toThrow(InvalidOperation)
    })
})