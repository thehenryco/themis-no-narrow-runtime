\# AI Session Handoff: RxRx3 End-to-End Themis Runtime



This file explains the end-to-end Themis/RxRx3 process for a new AI session or human reviewer.



It is not a biological claim file. It is a runtime, evidence, and verification handoff.



\## Public repo



Repository:



https://github.com/thehenryco/themis-no-narrow-runtime



Primary files:



\- ISSUE\_RXRX3\_COLLISION.md

\- evidence/rxrx3\_core\_public\_evidence\_card.json

\- evidence/rxrx3\_discovery\_voice\_card.json

\- docs/RXRX3\_SAMPLE\_SPEECH.md

\- evidence/rxrx3\_surface\_verification\_pack/

\- scripts/verify\_rxrx3\_collision.py

\- tests/public\_harness.py



Primary commits:



\- 22628f5 Add RxRx3 surface verification pack

\- 52bb6b2 Add RxRx3 maintainer issue draft



\## Boundary



Correct boundary:



\- Themis surface voice: emitted.

\- Final biological conclusion: not emitted.

\- Human verification: required.

\- Chat hidden-biology claim: not present.

\- New biological mechanism: not claimed.

\- PLK1 equals AKR1C3: not claimed.

\- Direct residual-atom-to-observed-collision link: not emitted.



A new AI session must not convert the surface event into a final biology claim.



\## What Themis saw



Dataset:



RxRx3-core



Observed event:



same 384-feature embedding digest across distinct metadata identities



Shared digest:



923e8f259a606dd40355f0fe0b2cecc473dd3755cf7b3ed9c2403c34e2423d60



Duplicate rows:



| sample\_index | well\_id | experiment\_name | plate | address | gene | treatment | perturbation\_type | cell\_type | well\_type\_label |

|---:|---|---|---:|---|---|---|---|---|---|

| 192182 | gene-134\_2\_L39 | gene-134 | 2 | L39 | PLK1 | PLK1\_guide\_1 | CRISPR | HUVEC | CRISPR Gene Positive Controls |

| 192184 | gene-134\_2\_N26 | gene-134 | 2 | N26 | AKR1C3 | AKR1C3\_guide\_5 | CRISPR | HUVEC | Query guides |



\## Runtime object



The runtime carried:



theta\_axis10\_residual\_star



Closure state:



CLOSED\_WITH\_RESIDUAL\_CARRIED



Residual tuple:



theta\_axis10\_residual\_star = (a9, a5, a7, a8, delta\_hidden)



Observed values:



\- a9 unresolved/void residual: 1.5282207919307684

\- a5 gap/surface: 0.7638888888888888

\- a7 raw/phase residual: 0.00022150707649535271

\- a8 boundary/closure residual: 0.7641103959653842

\- visible\_sum: 1.5282207919307684

\- delta\_hidden: 0.0

\- a10 equilibrium/rest: 0.6328875746760656



Important boundary:



The residual atoms are emitted as abstract-layer fields. The visible collision surface is emitted. A direct atom-to-observed-collision link is not emitted.



\## End-to-end process



\### 1. Clone or update repo



cd C:\\Users\\jerod

git clone https://github.com/thehenryco/themis-no-narrow-runtime.git

cd C:\\Users\\jerod\\themis-no-narrow-runtime



If the repo already exists:



cd C:\\Users\\jerod\\themis-no-narrow-runtime

git pull origin main



\### 2. Install verifier environment



cd C:\\Users\\jerod\\themis-no-narrow-runtime

python -m venv .venv\_public

.\\.venv\_public\\Scripts\\Activate.ps1

python -m pip install -U pip

python -m pip install -r requirements-rxrx3.txt



\### 3. Run duplicate verifier



The raw RxRx3-core data is not included in the repo.



Use a local RxRx3-core path:



<path-to-local-rxrx3\_core>



Run:



python scripts\\verify\_rxrx3\_collision.py --rxrx3-dir <path-to-local-rxrx3\_core>



Expected:



RXRX3 COLLISION VERIFIER: PASS



\### 4. Run public harness



cd C:\\Users\\jerod\\themis-no-narrow-runtime

python .\\tests\\public\_harness.py



Expected:



THEMIS PUBLIC HARNESS: PASS



Expected checks:



\- no\_confidential\_tracked\_files: true

\- no\_secret\_patterns\_detected: true

\- rxrx3\_public\_evidence\_card\_valid: true

\- duplicate\_embedding\_collision\_preserved: true



\## Result cards



\### Public evidence card



File:



evidence/rxrx3\_core\_public\_evidence\_card.json



Purpose:



Records the public duplicate embedding event.



It proves:



\- the duplicate representation surface exists in the inspected RxRx3-core carrier,

\- the two rows preserve distinct metadata identities,

\- the event is reproducible by the public verifier.



It does not prove:



\- PLK1 equals AKR1C3,

\- a biological mechanism,

\- whether the duplicate is expected behavior,

\- whether the duplicate is a data/export issue.



\### Discovery voice card



File:



evidence/rxrx3\_discovery\_voice\_card.json



Purpose:



Carries the Themis/Sefer voice state for the event.



Correct reading:



The event is not erased. It becomes a carried-residual discovery record.



\### Surface verification pack



Folder:



evidence/rxrx3\_surface\_verification\_pack/



Purpose:



Preserves the full current Themis surface for humans.



Correct boundary:



\- Themis surface voice: emitted.

\- Final biological conclusion: not emitted.

\- Human verification: required.

\- Chat hidden-biology claim: not present.

\- New biological mechanism: not claimed.

\- PLK1 equals AKR1C3: not claimed.



\### Full current Themis surface voice



File:



evidence/rxrx3\_surface\_verification\_pack/THEMIS\_FINAL\_FULL\_CURRENT\_SURFACE\_VERIFICATION\_VOICE.md



Purpose:



This is the final current surface voice for human verification.



Correct reading:



Themis reports an exact representation duplicate across distinct metadata identities, preserves the identity gap, carries theta\_axis10\_residual\_star, and routes the event into a verification frontier rather than a final biological mechanism.



\### Full surface layer voice



File:



evidence/rxrx3\_surface\_verification\_pack/THEMIS\_FULL\_SURFACE\_LAYER\_VOICE.md



Purpose:



Shows source paths, raw values, and pointer status.



Critical result:



\- residual atoms: ABSTRACT\_LAYER\_ONLY

\- visible surface fields: SURFACE\_PRESENT\_NO\_ATOM\_LINK

\- direct atom-to-observed-collision relation: NOT\_EMITTED\_IN\_SOURCE\_FIELDS



\### Biological frontier English



File:



evidence/rxrx3\_surface\_verification\_pack/RXRX3\_BIOLOGICAL\_FRONTIER\_SEFER\_ENGLISH.md



Purpose:



Explains the emitted surface in English as a verification frontier.



The event opens four verification paths:



1\. identity accounting,

2\. metadata alignment,

3\. biological review,

4\. frontier discovery.



It does not assert a new biological mechanism.



\## Human verification protocol



Humans or maintainers should verify:



1\. Re-read or recompute the 384-feature vectors for gene-134\_2\_L39 and gene-134\_2\_N26.

2\. Confirm the shared digest from original feature rows.

3\. Confirm both metadata rows.

4\. Verify metadata-to-embedding row alignment.

5\. Verify whether source images are distinct.

6\. Audit feature extraction or export duplication.

7\. Ask a domain scientist whether this PLK1 guide/control and AKR1C3 query guide pair should ever collapse at representation level.

8\. Build a review queue for exact embedding duplicates across distinct metadata identities.



Only after human/domain verification should any scientific conclusion be promoted beyond the current surface frontier.



\## Hugging Face manual upload



Create a Hugging Face Dataset repo, not a model repo.



Suggested repo:



thehenryco/rxrx3-surface-verification-pack



Manual upload source folder:



C:\\Users\\jerod\\themis-no-narrow-runtime\\evidence\\rxrx3\_surface\_verification\_pack



Upload only the verification pack files.



Do not upload:



\- raw RxRx3-core data,

\- private Themis runs,

\- private Sefer DB files,

\- .env,

\- tokens,

\- private local paths.



\## What a new AI session must not do



Do not claim:



\- PLK1 equals AKR1C3.

\- The two perturbations are biologically equivalent.

\- The duplicate digest is proven to be a data-pipeline error.

\- The duplicate digest is proven to be intended representation degeneracy.

\- a9, a5, a7, or a8 directly explain the observed collision.

\- A new biological mechanism has been discovered.

\- The human-verified scientific conclusion is complete.



\## What a new AI session may say



Themis has emitted a surface verification frontier. The event is an exact 384-feature embedding digest shared across distinct metadata identities. The runtime preserves the identity gap and carries it as theta\_axis10\_residual\_star under CLOSED\_WITH\_RESIDUAL\_CARRIED. The final biological meaning is not emitted and requires human verification.



\## Final one-line state



Themis emitted the current surface verification voice, not a final biological conclusion. The repo and optional Hugging Face upload should carry the evidence, hashes, result cards, and human verification protocol without Chat forcing hidden biology.

S 

