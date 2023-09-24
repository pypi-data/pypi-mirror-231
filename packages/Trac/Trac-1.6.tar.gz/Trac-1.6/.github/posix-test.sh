#! /bin/sh

set -ex

init_postgresql() {
    case "$MATRIX_OS" in
      ubuntu-*)
        sudo systemctl start postgresql.service
        ;;
      macos-*)
        rm -rf /usr/local/var/postgres
        pg_ctl initdb --pgdata /usr/local/var/postgres
        pg_ctl -w start --pgdata /usr/local/var/postgres --log /usr/local/var/postgres/postgresql.log || {
            echo "Exited with $?"
            cat /usr/local/var/postgres/postgresql.log
            exit 1
        }
        createuser -s postgres
        ;;
    esac
    {
        case "$MATRIX_OS" in
          ubuntu-*)
            sudo -u postgres psql -e
            ;;
          macos-*)
            psql -U postgres -e
            ;;
        esac
    } <<_EOS_
CREATE USER tracuser NOSUPERUSER NOCREATEDB CREATEROLE PASSWORD 'password';
CREATE DATABASE trac OWNER tracuser;
_EOS_
}

init_mysql() {
    case "$MATRIX_OS" in
      ubuntu-*)
        sudo systemctl start mysql.service
        {
            echo '[client]'
            echo 'host = localhost'
            echo 'user = root'
            echo 'password = root'
        } >~/.my.cnf
        ;;
      macos-*)
        brew install mysql
        mysql.server start
        {
            echo '[client]'
            echo 'host = localhost'
            echo 'user = root'
        } >~/.my.cnf
        ;;
    esac
    mysql -v <<_EOS_
CREATE DATABASE trac DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
CREATE USER tracuser@'%' IDENTIFIED BY 'password';
GRANT ALL ON trac.* TO tracuser@'%';
FLUSH PRIVILEGES;
_EOS_
}

run_tests() {
    case "$MATRIX_TRACDB" in
      postgresql)
        init_postgresql
        ;;
      mysql)
        init_mysql
        ;;
    esac

    (
        case "$MATRIX_OS" in
          macos-*)
            LDFLAGS='-L/usr/local/opt/openssl/lib'
            export LDFLAGS
            ;;
        esac
        pip install -r .github/requirements.txt
    )
    pip list --format=freeze

    case "$MATRIX_TRACDB" in
      sqlite)
        tracdb_uri='sqlite:test.db'
        ;;
      postgresql)
        echo "PostgreSQL: $(PGPASSWORD=password psql -h 127.0.0.1 -U tracuser trac -t -c 'SELECT version()')"
        tracdb_uri='postgres://tracuser:password@localhost/trac?schema=tractest'
        ;;
      mysql)
        echo "MySQL: $(mysql -sN -e 'SELECT version()')"
        tracdb_uri='mysql://tracuser:password@localhost/trac?charset=utf8mb4'
        ;;
      *)
        tracdb_uri=
        ;;
    esac
    {
        echo ".uri = $tracdb_uri"
        echo 'pythonopts = -Wdefault'
    } >Makefile.cfg
    make Trac.egg-info compile
    rc=0
    make unit-test || rc=$?
    if [ "$MATRIX_TESTS" = functional ]; then
        make functional-test testopts=-v || rc=$?
    fi
    return $rc
}

case "$MATRIX_OS" in
  ubuntu-*)
    sudo apt-get update -qq
    sudo apt-get install -qq -y subversion
    ;;
  macos-*)
    HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK=1
    export HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK
    brew update || :
    brew install subversion
    ;;
esac

venvdir="$HOME/venv"
python -m venv "$venvdir"
python="$venvdir/bin/python"
. "$venvdir/bin/activate"
"$python" -m pip install --upgrade pip setuptools

run_tests
