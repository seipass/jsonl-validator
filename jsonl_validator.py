import argparse,csv,json,sys
def transform(value):
    results=[]
    for number,line in enumerate(value.splitlines(),1):
        if not line.strip(): continue
        try: results.append({"line":number,"valid":True,"value":json.loads(line)})
        except json.JSONDecodeError as e: results.append({"line":number,"valid":False,"error":e.msg})
    return results

def main():
    parser=argparse.ArgumentParser(description='JSON Lines validator')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    result=transform(source)
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
