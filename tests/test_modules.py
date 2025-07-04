import builtins
import dns.resolver
import pytest

from modules import ip_tracker, dns_lookup, whois_lookup


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
