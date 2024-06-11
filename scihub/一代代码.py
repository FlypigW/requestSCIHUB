if __name__ == '__main__':
    # bib file address
    file_tix = r"bib\scopus.bib"
    # File storage address
    save_tix = r"paper\\"
    if not os.path.exists(save_tix):
        os.makedirs(save_tix)
    # find_way = 2,it's by DOI. find_way = 3,it's by Title
    find_way = 2
    paper_find = into_bib(file_tix)
    print("Bib contains {num} papers".format(num=len(paper_find[1])))
    if find_way is 2 and len(paper_find[1]) != len(paper_find[2]):
        print("Records contain missing BOI records. Please select the search method as paper title search, "
              "or complete (delete) the missing DOI records")
        # sys.exit()
    download_code = []
    for tix_num in range(len(paper_find[1])):
        print('NO.{num} Searching...'.format(num=tix_num + 1))
        downUrl = search_paper(paper_find[find_way][tix_num])
        if downUrl is None:
            print('NO.{num} Not found!'.format(num=tix_num + 1))
            download_code.append(tix_num + 1)
        else:
            print('NO.{num} Paper link:{paper_link}'.format(
                num=tix_num + 1, paper_link=downUrl))
            print('Downloading...')
            pdf = download_paper(downUrl)
            paper_name = paper_find[0][tix_num] + paper_find[1][tix_num]
            with open('%s.pdf' % (save_tix + paper_name), 'wb') as f:
                f.write(pdf)
            print('---Download complete---')
        time.sleep(0.8)
    print("The papers records not found are NO.{num}".format(
        num=download_code))
    print("The title of papers that was not found are:")
    for ii in range(len(download_code)):
        print("NO.{num}: {title}".format(
            num=download_code[ii], title=paper_find[3][download_code[ii] - 1]))