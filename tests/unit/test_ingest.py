from src.ingestion.ingest_users import run
from pathlib import Path


def test_run(tmp_path):
    src = tmp_path / "users.csv"
    src.write_text("user_id,name,email,created_at\n1,A,a@x.com,2025-01-01\n")

    landing = tmp_path / "landing"
    output = run(str(src), str(landing))

    assert Path(output).exists()
