import builtins
import dns.resolver
import pytest
import socket

from modules import (
    ip_tracker,
    dns_lookup,
    whois_lookup,
    github_user_scanner,
    port_scanner,
)


def test_ip_tracker_success(requests_mock, monkeypatch, capsys):
    mock_data = {
        "status": "success",
        "query": "1.1.1.1",
        "country": "Test",
        "regionName": "Test",
        "city": "Test",
        "isp": "Test",
        "org": "Test",
        "lat": 0,
        "lon": 0,
    }
    requests_mock.get(ip_tracker.API_URL + "1.1.1.1", json=mock_data)
    monkeypatch.setattr(builtins, "input", lambda _: "1.1.1.1")
    ip_tracker.run()
    captured = capsys.readouterr()
    assert "1.1.1.1" in captured.out


def test_dns_lookup_nxdomain(monkeypatch, capsys):
    def mock_resolve(domain, record):
        raise dns.resolver.NXDOMAIN
    monkeypatch.setattr(dns.resolver, "resolve", mock_resolve)
    monkeypatch.setattr(builtins, "input", lambda _: "example.com")
    dns_lookup.run()
    captured = capsys.readouterr()
    assert "Domain not found" in captured.out


def test_whois_lookup_invalid(monkeypatch, capsys):
    def mock_whois(domain):
        raise Exception("invalid")
    monkeypatch.setattr(whois_lookup.whois, "whois", lambda d: mock_whois(d))
    monkeypatch.setattr(builtins, "input", lambda _: "invalid")
    whois_lookup.run()
    captured = capsys.readouterr()
    assert "Invalid domain" in captured.out


def test_github_user_scanner_success(requests_mock, monkeypatch, capsys):
    mock_data = {
        "login": "octocat",
        "public_repos": 10,
        "followers": 100,
        "following": 2,
        "html_url": "https://github.com/octocat",
    }
    requests_mock.get(github_user_scanner.API_URL + "octocat", json=mock_data)
    monkeypatch.setattr(builtins, "input", lambda _: "octocat")
    github_user_scanner.run()
    captured = capsys.readouterr()
    assert "octocat" in captured.out


def test_port_scanner_simple(monkeypatch, capsys):
    inputs = iter(["localhost", "80-81"])

    class FakeSocket:
        def __init__(self, *args, **kwargs):
            self.addr = None

        def settimeout(self, timeout):
            pass

        def connect_ex(self, addr):
            self.addr = addr
            return 0 if addr[1] == 80 else 1

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            pass

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr(socket, "socket", lambda *a, **k: FakeSocket())
    port_scanner.run()
    captured = capsys.readouterr()
    assert "Port 80 open" in captured.out

