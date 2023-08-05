
export class InvalidOperation extends Error {
}


export const shortenText = (text: string, maxLength: number): string => {
    if (maxLength <= 3) {
        throw new InvalidOperation('Unable to shorten text to 3 characters or lower, Update with longer maxLength')
    }
    if (text.length > maxLength) {
        const substr = text.substring(0, maxLength - 3)
        return `${substr}...`
    }
    return text
}