
Maid.rules do

  rule 'move 2017 journal files into folder' do
    move(dir('~/Next/Journal/2017*.markdown'), '~/Next/Journal/2017')
  end

  rule 'move reminder call sheets into folder' do
    move(dir('~/Next/Scans/*Nursery Reminder Calls.pdf'), '~/Next/Administration/Nursery/Reminder Calls')
  end
  
  rule 'move nursery sign in sheets into folder' do
    move(dir('~/Next/Scans/*Nursery Worker Sign In Sheet.pdf'), '/home/wadeallen/Next/Administration/Nursery/Sign In Sheets')
  end

  rule 'move giving reports into folder' do
    move(dir('~/Next/Scans/*Giving Report.pdf'), '~/Next/Administration/Giving Reports')
  end

  rule 'move benefit wallet receipts into folder' do
    move(dir('~/Next/Scans/Benefit Wallet*.pdf'), '~/Next/Receipts/Medical/Benefit Wallet Receipts')
  end

  rule 'move church receipts into folder' do
    move(dir('~/Next/Scans/*Church Receipt*.pdf'), '~/Next/Receipts/Church/Current')
  end

  rule 'move housing receipts into folder' do
    move(dir('~/Next/Scans/*Housing Receipt*.pdf'), '~/Next/Receipts/Housing/Misc Housing')
  end

  rule 'move Comcast Bill into folder' do
    move(dir('~/Desktop/Comcast Bill*.pdf'), '~/Next/Receipts/Housing/Comcast')
  end

  rule 'move Kohls Statement into folder' do
    move(dir('~/Next/Scans/Kohls Statement*.pdf'), '~/Next/Statements/Kohls')
  end

  rule 'move American Eagle Statement into folder' do
    move(dir('~/Next/Scans/American Eagle Statement*.pdf'), '~/Next/Statements/American Eagle')
  end

  rule 'move Indiana Michigan Power Statement into folder' do
    move(dir('~/Desktop/I&MBill_*.pdf'), '~/Next/Receipts/Housing/Utilities/Electric')

  rule 'move School Receipts into folder' do
    move(dir('~/Next/Scans/*School Receipt*.pdf'), '~/Next/Receipts/School')
  end

  rule 'move Yorktown Muncipal Utilities into folder' do
    move(dir('~/Next/Scans/Yorktown Municipal Utilities*.pdf'), '~/Next/Receipts/Housing/Utilities/Water')
  end

  rule 'move Maurices Statement into folder' do
    move(dir('~/Next/Scans/Maurices*.pdf'), '~/Next/Statements/Maurices')
  end
  rule 'move Target Statement into folder' do
    move(dir('~/Next/Scans/Target Card*.pdf'), '~/Next/Receipts/Target')
  end

  rule 'move TJ Maxx Statement into folder' do
    move(dir('~/Next/Scans/TJ Maxx Statement*.pdf'), '~/Next/Receipts/TJ Maxx')
  end

  rule 'move Victoria Secret Statement into folder' do
    move(dir('~/Next/Scans/Victoria Secret Statement*.pdf'), '~/Next/Receipts/Victoria Secret')
  end

  rule 'move Childrens Place Statement into folder' do
    move(dir('~/Next/Scans/Childrens Place Statement*.pdf'), '~/Next/Receipts/Childrens Place')
  end

  rule 'move ATT Statement into folder' do
    move(dir('~/Desktop/ATT_Bill_*.pdf'), '~/Next/Receipts/Wireless Phone')
  end

  rule 'move IU Health Statement into folder' do
    move(dir('~/Next/Scans/IU Health Insurance*.pdf'), '~/Next/Receipts/Insurance/Health Insurance/IU Health Insurance')
  end

  rule 'move MD Wise Statement into folder' do
    move(dir('~/Next/Scans/MD Wise*.pdf'), '~/Next/Receipts/Insurance/Health Insurance/MD Wise Wade Christy')
  end

  rule 'move Vectren Bill into folder' do
    move(dir('~/Desktop/Vectren*.pdf'), '~/Next/Receipts/Housing/Utilities/Gas')
  end

  end
end


