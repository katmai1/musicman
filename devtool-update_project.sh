#
# Script to convert qt ui files and resources to python files
#

function info {
    echo -e " [i] $1"
}

#

function build_icons {
    echo -e "\tFile: 'icons/icons.qrc'"
    pyrcc5 icons/icons.qrc -o icons_rc.py
}

#

function build_UiFiles {
    for input_file in ui/*
    do
        output_file=${input_file/.ui/_Ui.py}
        echo -e "\t'$input_file' to '$output_file'..."
        pyuic5 -o app/$output_file $input_file
    done
}

#

function build_project_file {
    echo " " > project.pro
    find . -type f -name "*.py" | while read filename
    do
        echo "SOURCES += $filename" >> project.pro
    done
    echo "TRANSLATIONS += app/i18n/en_EN.ts" >> project.pro
    echo "TRANSLATIONS += app/i18n/es_ES.ts" >> project.pro
    pylupdate5 -noobsolete project.pro
    # pylupdate5 project.pro
    lrelease project.pro
}

# inicio

header

info "Icon Resources"
build_icons

info "Ui Files"
build_UiFiles

build_project_file
