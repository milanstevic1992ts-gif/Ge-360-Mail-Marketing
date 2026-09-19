# Architettura GE360 Mail Marketing

## Regola principale

GE360 Core è l'orchestratore e la fonte di identità interna. I motori esterni non devono integrarsi direttamente fra loro.

```
               +----------------+
               |   GE360 Core   |
               +--------+-------+
                        |
        +---------------+----------------+
        |               |                |
     Prospex          Twenty           Mautic
        |               |                |
        +---------------+----------------+
                        |
                    OpenCRM
```

## Responsabilità

- **GE360 Core**: identità contatti, deduplica, policy, audit, orchestrazione, mapping ID esterni.
- **Prospex**: discovery/enrichment lead.
- **Twenty**: CRM operativo.
- **Mautic**: segmenti, campagne, eventi email.
- **OpenCRM**: pipeline/AI commerciale sperimentale.
- **Jarvis**: livello assistivo successivo; non deve bypassare le policy del core.

## Identità

Ogni contatto riceve un `ge360_id` stabile, ad esempio `CNT-ABC123DEF456`.

Gli ID esterni sono salvati in `external_identities` e sono univoci per coppia `engine + external_id`.

## Regola integrazioni

Nessun endpoint upstream viene inventato. Ogni adapter viene implementato soltanto dopo verifica della documentazione/versione effettivamente installata del motore.

## Database

v0.1 usa SQLAlchemy e PostgreSQL. `create_all` è solo bootstrap di sviluppo; prima della release verranno introdotte migrazioni Alembic.

## Sicurezza

- segreti solo da environment/.env locale;
- nessuna API key nel repository;
- flag `do_not_contact` centrale;
- stato marketing separato dallo stato commerciale;
- audit e suppression list previsti prima dell'invio campagne.
