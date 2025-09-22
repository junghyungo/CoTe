function solution(id_list, report, k) {
    const reported_id = new Map(id_list.map(id => [id, 0]));
    const reporter_id = new Map(id_list.map(id => [id, 0]));
    
    report = new Set(report);
    report.forEach((r) => {
        const reported = r.split(' ')[1];
        const cnt = reported_id.get(reported);
        reported_id.set(reported, cnt+1);
    });
    
    report.forEach((r) => {
        const reporter = r.split(' ')[0];
        const reported = r.split(' ')[1];
        
        if (reported_id.get(reported) >= k) {
            const cnt = reporter_id.get(reporter);
            reporter_id.set(reporter, cnt+1);
        }
    });
    
    return [...reporter_id.values()];
}