# Command line utility to send attachments to your kindle
# It supports sending a PDF in both regular form and with the convert option
# and sending to the regular (@kindle.com) or free Kindle mail (@free.kindle.com)

# The only argument it has is the name of the file to send. It will detect if
# it is a pdf and treat it accordingly.

## Preferences
# If true, send one version with pdf as-is, another with 'convert' subject
# else, just send the pdf version
SEND_PDF_BOTH_VERSIONS=false

# if true, sends file to @free.kindle.com instead of @kindle.com
SEND_TO_FREE_MAIL=false

## Configuration. Change the base username to fit your needs
BASE_USERNAME="wade_5499"
BASE_KINDLE_MAIL="$BASE_USERNAME@kindle.com"
FREE_KINDLE_MAIL="$BASE_USERNAME@free.kindle.com"

## Helper functions
# Prints confirmation message
_confirmation() {
    echo "$1 sent to $2 with subject \"$3\""
}

# Prints error message
_error() {
    echo "There was an error sending $1 to $2 with subject \"$3\""
}

#Sends an email
# $1 is the path to the attachment
# $2 is the recipient of the email (i.e. To: example@kindle.com)
# $3 OPTIONAL The subject of the email
_send() {
    local attachment=$1
    local mail=$2
    if ! [[ $3 ]]; then
        subject="kindle cli"
    else
        subject=$3
    fi
    # Send mail
    mutt -s $subject -a $attachment -- $mail < /dev/null
    if [[ $? -ne 0 ]]; then
        _error $attachment $mail $subject
    else
        _confirmation $attachment $mail $subject
    fi

}
# $1 is the name of the attachment file
# $2 is the subject of the mail. You shold set this to 'convert'
_send_mail() {
    if $SEND_TO_FREE_MAIL; then
        _send $1 $FREE_KINDLE_MAIL $2
    else
        _send $1 $BASE_KINDLE_MAIL $2
    fi
}

## Main script
# If mutt not found then exit
command -v mutt >/dev/null 2>&1 || { echo >&2 "Mutt is required but it was not found. Please install it"; exit 1; }

filename=$1
_send_mail $1
exit 0
