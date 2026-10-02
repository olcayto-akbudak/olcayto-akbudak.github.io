# Analist GitHub Laboratuvarları

Bu koleksiyon 10 bağımsız ileri seviye proje içerir. Her projede çalışan motor, sentetik senaryo ve 8 alan testi bulunur. Tam Türkçe teknik belgeler ve CI tanımı bağımsız ZIP paketlerindedir. Diğer 10 proje profil sahibinin ayrı GitHub depolarında yayımlanmıştır.

GitHub yeni depo oluşturma hız sınırı nedeniyle bu 10 proje mevcut portföy deposunda yayımlanmıştır. Kaynak dosyalar doğrudan okunabilir; bağımsız ZIP paketleri tek başına çalışır.

| No | Proje ve README | Kaynak kod | Bağımsız paket |
|---|---|---|---|
| 11 | [Mevsimsel Anomali Konsensüsü](anomaly-consensus-engine-README.md) | [anomaly_consensus_engine.py](anomaly_consensus_engine.py) | [Paket](anomaly-consensus-engine.zip) |
| 12 | [Kısıtlı Müşteri Eşleştirme](entity-resolution-workbench-README.md) | [entity_resolution_workbench.py](entity_resolution_workbench.py) | [Paket](entity-resolution-workbench.zip) |
| 13 | [Gereksinim ve Test İzlenebilirliği](requirements-traceability-graph-README.md) | [requirements_traceability_graph.py](requirements_traceability_graph.py) | [Paket](requirements-traceability-graph.zip) |
| 14 | [Entegrasyon Test DAG Orkestratörü](integration-test-orchestrator-README.md) | [integration_test_orchestrator.py](integration_test_orchestrator.py) | [Paket](integration-test-orchestrator.zip) |
| 15 | [Sipariş Saga ve Telafi Laboratuvarı](order-saga-recovery-README.md) | [order_saga_recovery.py](order_saga_recovery.py) | [Paket](order-saga-recovery.zip) |
| 16 | [SLA ve Çok Pencereli Burn Rate](sla-error-budget-monitor-README.md) | [sla_error_budget_monitor.py](sla_error_budget_monitor.py) | [Paket](sla-error-budget-monitor.zip) |
| 17 | [Tenant Adil Kuyruk Motoru](tenant-fair-queue-README.md) | [tenant_fair_queue.py](tenant_fair_queue.py) | [Paket](tenant-fair-queue.zip) |
| 18 | [Dayanıklı Proje Portföyü Optimizasyonu](robust-portfolio-optimizer-README.md) | [robust_portfolio_optimizer.py](robust_portfolio_optimizer.py) | [Paket](robust-portfolio-optimizer.zip) |
| 19 | [Veri Sözleşmesi ve Karantina](data-contract-quality-gate-README.md) | [data_contract_quality_gate.py](data_contract_quality_gate.py) | [Paket](data-contract-quality-gate.zip) |
| 20 | [SQL Doğruluk ve Plan Regresyonu](sql-plan-regression-lab-README.md) | [sql_plan_regression_lab.py](sql_plan_regression_lab.py) | [Paket](sql-plan-regression-lab.zip) |

## Tüm koleksiyon testleri

Bu klasörde:

```bash
python -m unittest discover -s . -p "test_*.py" -v
```

80 test; dış paket gerekmez. Her projenin motor dosyasını `python <dosya>.py demo` ile çalıştırabilirsiniz. Windows üzerinde SQLite bağlantılarının transaction sonrası kapanması test edilir. Örnekler tamamen sentetiktir.
