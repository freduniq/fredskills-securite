<?php
// Exemple générique à adapter ; les paramètres de connexion proviennent d'un fournisseur de secrets.
// Ne jamais committer un vrai mot de passe ni afficher l'exception en production.
function findInvoiceForTenant(PDO $pdo, int $tenantId, int $invoiceId): ?array {
    $stmt = $pdo->prepare('SELECT id, reference, total_ttc FROM invoices WHERE id = :id AND tenant_id = :tenant LIMIT 1');
    $stmt->execute([':id' => $invoiceId, ':tenant' => $tenantId]);
    $invoice = $stmt->fetch(PDO::FETCH_ASSOC);
    return $invoice ?: null;
}

function safeHtml(string $value): string {
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}
