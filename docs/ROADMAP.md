# Roadmap operativa

## v0.1 - Core orchestratore

Stato: **IN CORSO**

Criteri di uscita:
- [x] repository inizializzata
- [x] FastAPI bootstrap
- [x] PostgreSQL + Redis via Docker Compose
- [x] modello Contact
- [x] mapping ExternalIdentity
- [x] contratti adapter Prospex/Twenty/Mautic/OpenCRM
- [x] endpoint health
- [x] endpoint base contatti
- [x] script doctor
- [ ] deduplica contatti
- [ ] audit event
- [ ] test automatici
- [ ] CI verde

## v0.2 - Twenty + Prospex

Criteri di uscita:
- [ ] verificare API/versioni upstream
- [ ] adapter Twenty reale
- [ ] adapter Prospex reale
- [ ] import lead Prospex -> GE360
- [ ] push GE360 -> Twenty
- [ ] gestione conflitti
- [ ] sync controllata e idempotente

## v0.3 - Mautic

- [ ] adapter reale
- [ ] segmenti
- [ ] campagne
- [ ] webhook eventi
- [ ] suppression list
- [ ] audit invii

## v0.4 - OpenCRM + Jarvis

- [ ] adapter OpenCRM
- [ ] opportunità
- [ ] inbox
- [ ] comandi Jarvis
- [ ] approvazioni umane

## v0.5 - Pacchetto Debian

- [ ] systemd
- [ ] postinst/prerm
- [ ] backup/restore/update
- [ ] build .deb
- [ ] release GitHub Actions

## Decisioni bloccate

1. GE360 possiede l'identità interna.
2. I motori esterni restano separati.
3. Nessuna dipendenza diretta Prospex <-> Twenty <-> Mautic <-> OpenCRM.
4. Nessun endpoint upstream viene ipotizzato.
5. Prima integrazione reale: Twenty + Prospex.
